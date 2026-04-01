function uploadResume() {
    let fileInput = document.getElementById("resume");
    let loader = document.getElementById("loader");
    let resultDiv = document.getElementById("result");

    if (fileInput.files.length === 0) {
        alert("Please upload a file");
        return;
    }

    loader.classList.remove("hidden");
    resultDiv.innerHTML = "";

    let formData = new FormData();
    formData.append("resume", fileInput.files[0]);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        loader.classList.add("hidden");

        let skillsHTML = "";
        data.skills.forEach(skill => {
            skillsHTML += `<span class="skill">${skill}</span>`;
        });

        resultDiv.innerHTML = `
            <h3>Analysis Result</h3>
            <p><b>Score:</b> ${data.score}</p>
            <p><b>Suggestion:</b> ${data.suggestion}</p>
            <div>${skillsHTML}</div>
        `;
    });
}
