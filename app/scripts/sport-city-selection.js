export class SportCitySelection {
    constructor() {
        document.querySelector('.selected-sport').addEventListener('click', () => {
            this.toggleSportSelection();
        });

        document.querySelector('.selected-center').addEventListener('click', () => {
            this.toggleCitySelection();
        });
        var el = document.querySelectorAll('.selected-sport + .custom-select li');
        for (var i = 0; i < el.length; i++) {
            el[i].addEventListener('click', (e) => {
                this.showSportSelected(e);
            }, false);
        }

        var el = document.querySelectorAll('.selected-center  + .custom-select li');
        for (var i = 0; i < el.length; i++) {
            el[i].addEventListener('click', (e) => {
                this.showCenterSelected(e);
            }, false);
        }
        document.getElementsByClassName("submit-selection")[0].addEventListener('click', (e) => {
            this.submitSelection(e);
        });

    }
    toggleClass(el, className) {
        el.classList.toggle(className)
    }
    toggleSportSelection() {
        this.toggleClass(document.querySelector('.selected-sport'), 'active');
    }
    toggleCitySelection() {
        this.toggleClass(document.querySelector('.selected-center'), 'active');
    }
    showSportSelected(el) {
        document.getElementsByClassName("selected-sport")[0].innerHTML = el.target.innerHTML;
        document.getElementsByClassName("selected-sport")[0].classList.remove('active');
        document.getElementsByClassName("selected-sport")[0].classList.add('highlight');
        document.getElementsByClassName("selected-sport")[0].setAttribute("slug", el.target.getAttribute("slug"));
        document.getElementsByClassName("selected-sport")[0].setAttribute("sport", el.target.getAttribute("sport"));
    }
    showCenterSelected(el) {
        document.getElementsByClassName("selected-center")[0].innerHTML = el.target.innerHTML;
        document.getElementsByClassName("selected-center")[0].classList.remove('active');
        document.getElementsByClassName("selected-center")[0].classList.add('highlight');
        document.getElementsByClassName("selected-center")[0].setAttribute("center", el.target.getAttribute("center"));
        document.getElementsByClassName("selected-center")[0].setAttribute("slug", el.target.getAttribute("slug"));

    }
    submitSelection(e) {
        let center_id = parseInt(document.getElementsByClassName("selected-center")[0].getAttribute("center"));
        let sport_id = parseInt(document.getElementsByClassName("selected-sport")[0].getAttribute("sport"));
        let sport_slug = document.getElementsByClassName("selected-sport")[0].getAttribute("slug");
        let center_slug = document.getElementsByClassName("selected-center")[0].getAttribute("slug");

        if (sport_slug === null && center_slug != null) {
            location.href =`/center/${center_id}/${center_slug}`;
        }
        if (center_slug === null && sport_slug!= null) {
            location.href =`/sport/${sport_id}/${sport_slug}`;
        }
        if (center_slug != null && sport_slug!= null) {
            location.href =`/center/${center_id}/sports/${sport_slug}`;
        }
    }

}