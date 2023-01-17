// const openBtn = document.getElementById('game-config');
// const modalOverlay = document.querySelector('.game-setup-container');
// const closeSetup = document.querySelector('.game-setup-close');
// const contentBlur = document.getElementById('content');

// openBtn.addEventListener('click', () => {
//     modalOverlay.classList.add('open-modal');
//     contentBlur.classList.add('blur-bg');
// });

// closeSetup.addEventListener('click', () => {
//     modalOverlay.classList.remove('open-modal');
//     contentBlur.classList.remove('blur-bg');
// });

const boxBtn = document.querySelectorAll(".side-border");
const borderColor = document.querySelectorAll(".box");

boxBtn.forEach((boxes) => {
  const box = boxes.querySelector(".box");

  box.addEventListener("click", () => {
    boxBtn.forEach((item) => {
      if (item !== box) {
        item.classList.remove("side-border-main");
      }
    });

    boxes.classList.toggle("side-border-main");
  });

  box.addEventListener("click", () => {
    borderColor.forEach((boxesColor) => {
      if (boxesColor !== borderColor) {
        boxesColor.classList.remove("border-color");
      }
    });

    box.classList.toggle("border-color");
  });
});

// Project Page

const addMoreButton = document
  .querySelector(".project-plus-button")
  .addEventListener("click", () => {
    document.querySelector(
      ".project-content"
    ).innerHTML += `    <div class="box-content">
    <h3 class="project-title">Eagle Carbine</h3>
    <img src="/rimworld-toolkit-stable/icon.png" class="box-icon" alt="" />

    <div class="content-data">
      <label
        >Weapon Name
        <input type="text" class="project-inputs" />
      </label>

      <label
        >Weapon Damage
        <input type="text" class="project-inputs" />
      </label>

      <label
        >Weapon Range
        <input type="text" class="project-inputs" />
      </label>
    </div>
  </div>
  
  <div class="invisible-box-content"></div>`;
  });
