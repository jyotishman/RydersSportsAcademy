import {SportCitySelection} from "./sport-city-selection";
import {Slider} from "./slider";

export default class App {
	constructor(){
		this.init();
		this.sports = new SportCitySelection();
		this.slider = new Slider();
		
	}
	init() {

	}
}
const app = new App();