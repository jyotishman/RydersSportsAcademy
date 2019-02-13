export class SportCitySelection {
	constructor(){
		document.querySelector('.selected-sport').addEventListener('click', () => {
			this.toggleSportSelection();
		});

		document.querySelector('.selected-center').addEventListener('click', () => {
			this.toggleCitySelection();
		});
		var el = document.querySelectorAll('.custom-select li');
		for(var i=0; i < el.length; i++){
		    el[i].addEventListener('click',(e) => {
		        this.showSelected(e);
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
	showSelected(el) {
		document.getElementsByClassName("selected-sport").innerHTML(el.target.innerHTML)
	}

}
