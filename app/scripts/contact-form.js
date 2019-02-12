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
        request.onload = () => callback(request.responseText);
        request.onerror = () => err(request);
        request.send(data);
    };

    submitContactForm() {
        const newPost = {
            "full_name": document.getElementById('name').value,
            "email": document.getElementById('email').value,
            "content": document.getElementById('comment').value,
            "phone_number": '+91'+document.getElementById('phone').value
        };
        const data = JSON.stringify(newPost);
        this.httpPost(
            'api/v1/contact-us/',
            data,
            console.log
        );
    };



}