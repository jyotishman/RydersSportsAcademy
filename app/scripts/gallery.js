export class Gallery {
	constructor(){

		$(document).ready(function() {
			$(".fancybox-button").fancybox({
				helpers : {
			        title: {
			            type : 'float',
			            position: 'top'
			        }
			    },
			    nextEffect: 'fade',
		        prevEffect: 'fade'
			});
		});
	}
	
}
