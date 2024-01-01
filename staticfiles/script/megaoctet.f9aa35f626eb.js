const convertion = () => {
  const quantite = document.getElementById("quantite").value;
  const data = document.getElementById("data_forfait");
  const indic = document.getElementById("indic");

  const rate = 2;

  let dataForfait = quantite * rate;
  document.getElementById("data_forfait").value = dataForfait;

  indic.innerHTML = `<p>${quantite} crédits = ${dataForfait} Mo</p>`;
}

const quantiteValue = document.getElementById("quantite");
quantiteValue.addEventListener("input", convertion);
quantiteValue.addEventListener("change", convertion);

convertion();