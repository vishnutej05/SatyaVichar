document.getElementById("file-icon").addEventListener("click", function () {
  document.getElementById("file-input").click();
});

function genTxt() {
  const prompt = document.getElementById("prompt").value;
  const resultDiv = document.getElementById("result");
  const prDiv = document.createElement("div");
  const proSpan = document.createElement("span");
  prDiv.classList.add("fullStyling");
  proSpan.classList.add("prSpanStyling");
  proSpan.textContent = prompt;
  prDiv.style.textAlign = "right";
  prDiv.appendChild(proSpan);
  resultDiv.appendChild(prDiv);

  // Scroll to the bottom of the resultDiv
  resultDiv.scrollTop = resultDiv.scrollHeight;

  fetch("/textGen", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ prompt: prompt }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      const resDiv = document.createElement("div");
      const dataSpan = document.createElement("span");
      resDiv.classList.add("fullStyling", "resDivStyling");
      dataSpan.classList.add("resSpanStyling");
      dataSpan.innerHTML = data;

      resDiv.style.textAlign = "left";
      resDiv.appendChild(dataSpan);
      resultDiv.appendChild(resDiv);
      resultDiv.scrollTop = resultDiv.scrollHeight;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
