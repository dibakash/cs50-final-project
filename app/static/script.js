
let forms = document.getElementsByClassName("pallet");

// display colors for each color pallet
[...forms].forEach(form => {
    form.querySelectorAll('span')
        .forEach(span =>
            span.style.backgroundColor = span.dataset["clr"])
});


// document.addEventListener("click", function (e) {
//     if (e.target.classList.contains("btn")) {
//         let btn = e.target;
//         let pallet = btn.closest(".pallet")
//         console.log(pallet);
//         pallet.remove();
//     }

// })
