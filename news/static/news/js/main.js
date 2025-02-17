document.addEventListener("DOMContentLoaded", function() {
    loadPosts();
    setupAuth();
});

function loadPosts() {
    fetch("/api/posts/")
        .then(response => response.json())
        .then(posts => {
            const container = document.getElementById("posts-container");
            container.innerHTML = "";
            posts.forEach(post => {
                const postElement = document.createElement("div");
                postElement.classList.add("post");
                postElement.innerHTML = `
                    <h3>${post.title}</h3>
                    <p>By ${post.author__username} | ${post.created_at}</p>
                    <p>${post.content.substring(0, 100)}...</p>
                    <button class="vote-btn" data-post="${post.id}" data-vote="up">👍</button>
                    <button class="vote-btn" data-post="${post.id}" data-vote="down">👎</button>
                `;
                container.appendChild(postElement);
            });
            setupVoting();
        });
}

function setupVoting() {
    document.querySelectorAll(".vote-btn").forEach(button => {
        button.addEventListener("click", function() {
            const postId = this.dataset.post;
            const voteType = this.dataset.vote;
            fetch(`/api/posts/${postId}/vote/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ vote: voteType })
            })
            .then(response => response.json())
            .then(data => console.log("Vote Count:", data.votes));
        });
    });
}

function setupAuth() {
    document.getElementById("login-btn").addEventListener("click", function() {
        fetch("/api/login/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: "admin", password: "adminpass" })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            document.getElementById("login-btn").style.display = "none";
            document.getElementById("logout-btn").style.display = "inline";
        });
    });

    document.getElementById("logout-btn").addEventListener("click", function() {
        fetch("/api/logout/")
        .then(() => {
            alert("Logged out");
            document.getElementById("login-btn").style.display = "inline";
            document.getElementById("logout-btn").style.display = "none";
        });
    });
}