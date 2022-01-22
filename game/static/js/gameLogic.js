// self executing function - define here all functions in the row you want to execute them
(function() {
    mixQuestions()
 })();

//logic to mix the questions
function mixQuestions(){
    var ul = document.querySelector('.answers');
    for (var i = ul.children.length; i >= 0; i--) {
        ul.appendChild(ul.children[Math.random() * i | 0]);
    }
}

function deleteOneQuestion(rightQuestion){
    
    var lis = document.querySelectorAll('.answers li');
    random = Math.floor(Math.random() * lis.length);

    removedItem = lis[random]
    removedItemText = removedItem.innerText

    console.log("Removed item text: " + removedItemText)

    console.log("Removed item: " + removedItem)
    console.log("Right question: " + rightQuestion)

    if(removedItemText == rightQuestion){
        if(random < lis.length-1){
            random += 1;
        }else{
            random -= 1;
        }
    }   

    lis[random].remove()
    document.getElementById('deleteOneQuestionButton').remove()

}

