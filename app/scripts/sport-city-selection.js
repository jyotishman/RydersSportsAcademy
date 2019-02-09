export class SportCitySelection {
	constructor(){
		document.querySelector('.selected-sport').addEventListener('click', () => {
			this.toggleSportSelection();
		});

		document.querySelector('.selected-center').addEventListener('click', () => {
			this.toggleCitySelection();
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
}
