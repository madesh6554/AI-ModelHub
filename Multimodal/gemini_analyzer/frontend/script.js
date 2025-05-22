const fileInput = document.getElementById('fileInput');
const dropArea = document.getElementById('drop-area');
const urlInput = document.getElementById('urlInput');
const promptInput = document.getElementById('promptInput');
const responseArea = document.getElementById('responseArea');

dropArea.addEventListener("dragover", e => {
  e.preventDefault();
  dropArea.style.background = "#eee";
});

dropArea.addEventListener("dragleave", () => {
  dropArea.style.background = "white";
});

dropArea.addEventListener("drop", e => {
  e.preventDefault();
  dropArea.style.background = "white";
  fileInput.files = e.dataTransfer.files;
});

async function analyze() {
  const prompt = promptInput.value;

  if (fileInput.files.length > 0) {
    const formData = new FormData();
    formData.append("prompt", prompt);
    formData.append("file", fileInput.files[0]);

    const res = await fetch("http://127.0.0.1:8000/analyze/file", {
      method: "POST",
      body: formData
    });
    const data = await res.json();
    responseArea.innerText = data.result;
  } else if (urlInput.value.trim() !== "") {
    const res = await fetch("http://127.0.0.1:8000/analyze/url", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        url: urlInput.value,
        prompt: prompt
      })
    });
    const data = await res.json();
    responseArea.innerText = data.result;
  } else {
    alert("Please upload a file or paste a URL.");
  }
}
