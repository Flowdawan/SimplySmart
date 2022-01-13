// self executing function - define here all functions in the row you want to execute them
(function() {
    mixQuestions()
 })();

//logic to mix the questions
function mixQuestions(){
    var ul = document.querySelector('ul');
    for (var i = ul.children.length; i >= 0; i--) {
        ul.appendChild(ul.children[Math.random() * i | 0]);
    }
}

