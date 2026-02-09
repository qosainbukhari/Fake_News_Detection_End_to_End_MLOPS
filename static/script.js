async function predict() {
    const input = document.getElementById("newsInput");
    const resultDiv = document.getElementById("result");
    const resultIcon = document.getElementById("resultIcon");
    const resultText = document.getElementById("resultText");
    const loader = document.getElementById("loader");
    const btn = document.getElementById("predictBtn");

    const text = input.value.trim();
    if (!text) {
        alert("Please enter some news text.");
        return;
    }

    // Show loader, hide previous result
    resultDiv.classList.add("hidden");
    resultDiv.classList.remove("real", "fake");
    loader.classList.remove("hidden");
    btn.disabled = true;

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text }),
        });

        const data = await response.json();

        loader.classList.add("hidden");
        btn.disabled = false;

        if (data.prediction === "Real News") {
            resultDiv.classList.add("real");
            resultIcon.textContent = "\u2713";
            resultText.textContent = "Real News";
        } else {
            resultDiv.classList.add("fake");
            resultIcon.textContent = "\u2717";
            resultText.textContent = "Fake News";
        }

        resultDiv.classList.remove("hidden");
    } catch (error) {
        loader.classList.add("hidden");
        btn.disabled = false;
        alert("Error: Could not get prediction. Make sure the server is running.");
    }
}

// Allow Ctrl+Enter to submit
document.getElementById("newsInput").addEventListener("keydown", function (e) {
    if (e.ctrlKey && e.key === "Enter") {
        predict();
    }
});
