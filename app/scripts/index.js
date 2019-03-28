// import {SportCitySelection} from "./sport-city-selection";
import {Slider} from "./slider";

export default class App {
	constructor(){
		this.init();
		// this.sports = new SportCitySelection();
		this.slider = new Slider();

		
	}
	init() {
		let bLazy = new Blazy({
		  offset: 0,
		  selector: 'img',
		  loadInvisible: false,
		  success: function() {
		  }
		});
	}
}
const app = new App();