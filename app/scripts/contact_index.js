import {Contact} from "./contact-form";

export default class App {
	constructor(){
		this.init();
		this.contact = new Contact();
		
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