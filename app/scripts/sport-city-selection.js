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
    }
    showCenterSelected(el) {
        document.getElementsByClassName("selected-center")[0].innerHTML = el.target.innerHTML;
        document.getElementsByClassName("selected-center")[0].classList.remove('active');
    }

}