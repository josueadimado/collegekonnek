// Create an array for of questions
var questions = [
    'Analyze data using statistics?','Counsel people with drug or addiction?','Create art for sale and exhibition?','Direct the making of a movie?','Entertain an audience?','Estimate the value of items for an insurance policy?','Examine artifacts left behind by previous civilizations?','Find support resources for families in need ?'
]

    // function results(){
    //     window.open("https://vvu.edu.gh")
    // };

var i = 0;

$('#submit').click(function() {
        $('#question').html(questions[i]);
        $('#options').html(`<!--Material Radio-->
                                                    <label class="material-radio is-accent">
                                                        <input type="radio" name="group-demo1" >
                                                        <span class="dot"></span>
                                                        <span class="radio-label">Hate it</span>
                                                    </label>
                                                    <!--Material Radio-->
                                                    <label class="material-radio is-accent">
                                                        <input type="radio" name="group-demo1">
                                                        <span class="dot"></span>
                                                        <span class="radio-label">Dislike it</span>
                                                    </label>
                                                    <!--Material Radio-->
                                                    <label class="material-radio is-accent">
                                                        <input type="radio" name="group-demo1">
                                                        <span class="dot"></span>
                                                        <span class="radio-label">Neutral</span>
                                                    </label>
                                                    <!--Material Radio-->
                                                    <label class="material-radio is-accent">
                                                        <input type="radio" name="group-demo1">
                                                        <span class="dot"></span>
                                                        <span class="radio-label">Like it</span>
                                                    </label>
                                                    <!--Material Radio-->
                                                    <label class="material-radio is-accent">
                                                        <input type="radio" name="group-demo1">
                                                        <span class="dot"></span>
                                                        <span class="radio-label">Love it</span>
                                                    </label>`);
        i++;
        if(i === (questions.length)){
             window:location.href = "/result"
        }   
   
});