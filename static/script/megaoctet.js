const convertion = () => {
  const quantite = document.getElementById("quantite").value;
  const data_mo = document.getElementById("data_mo");
  const data = document.getElementById("data_forfait");

  const rate = 2;

  quantite >= 50 ? data.value = quantite * rate : data.value = 0;

  const calculatedValue = quantite >= 50 ? quantite * rate : 0;

  // data_mo show
  const displayValue = quantite >= 50 ? `${calculatedValue} Mo` : `0 Mo`;

  data.setAttribute("data-value", calculatedValue);
  data_mo.value = displayValue;
}

const quantiteValue = document.getElementById("quantite");
quantiteValue.addEventListener("input", convertion);
quantiteValue.addEventListener("change", convertion);

convertion();