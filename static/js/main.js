document.addEventListener("DOMContentLoaded", () => {
  const navToggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".main-nav");
  if (navToggle && nav) {
    navToggle.addEventListener("click", () => {
      nav.classList.toggle("active");
    });
  }

  const lightbox = document.getElementById("lightbox");
  if (lightbox) {
    const lightboxImage = lightbox.querySelector("img");
    const closeButton = lightbox.querySelector(".lightbox-close");

    document.querySelectorAll("[data-lightbox]").forEach((card) => {
      card.addEventListener("click", () => {
        const source = card.querySelector(".lightbox-source");
        if (source) {
          lightboxImage.src = source.src;
          lightbox.classList.add("active");
          lightbox.setAttribute("aria-hidden", "false");
        }
      });
    });

    const close = () => {
      lightbox.classList.remove("active");
      lightbox.setAttribute("aria-hidden", "true");
      lightboxImage.src = "";
    };

    closeButton?.addEventListener("click", close);
    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox) {
        close();
      }
    });
  }
});
