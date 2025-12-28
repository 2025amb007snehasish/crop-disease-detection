async function predict() {
    const input = document.getElementById("imageInput");
    const result = document.getElementById("result");

    if (input.files.length === 0) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();
    formData.append("file", input.files[0]);

    result.innerText = "Predicting...";

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        result.innerText = "Prediction: " + data.prediction;
    } catch (error) {
        result.innerText = "Error connecting to backend";
    }
}
