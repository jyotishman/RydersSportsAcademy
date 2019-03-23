import {Gallery} from "./gallery";

export default class App {
	constructor(){
		this.init();
		this.gallery = new Gallery();
		
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