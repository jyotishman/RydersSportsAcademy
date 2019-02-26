export class Contact {
    constructor() {

        document.getElementById('contact-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.submitContactForm();
        })
    }
    httpPost(url, data, callback, err = console.error) {
        const request = new XMLHttpRequest();
        request.open('POST', url, true);
        request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
        request.onload = () => {
            if (request.readyState === request.DONE) {
                    if (request.status === 200) {
                        callback(request.responseText);
                    }
                }
        }
        request.onerror = () => err(request);
        request.send(data);
    };

    submitContactForm() {
        document.getElementById('form_btn').classList.add('disable'); // Add class
        const newPost = {
            "full_name": document.getElementById('name').value,
            "sport": document.getElementById('sport-selection').value,
            "email": document.getElementById('email').value,
            "content": document.getElementById('comment').value,
            "phone_number": '+91'+document.getElementById('phone').value
        };
        const data = JSON.stringify(newPost);
        this.httpPost(
            'api/v1/contact-us/',
            data,
            (e)=>{
                let obj = JSON.parse(e)
                if (obj.send) {
                    document.getElementById("contact-form").reset();
                    document.getElementById('form_btn').classList.remove('disable'); // Add class

                    var x = document.getElementById("success-msgz");
                      x.style.display = "block";
                }
                
            }
        );
    };



}