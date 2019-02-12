import {SportCitySelection} from "./sport-city-selection";
import {Gallery} from "./gallery";

export default class App {
	constructor(){
		this.init();
		this.sports = new SportCitySelection();
		this.gallery = new Gallery();
		
	}
	init() {

	}
}
const app = new App();