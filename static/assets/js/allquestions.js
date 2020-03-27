// Create an array for of questions
var questions = [
    'Analyze data using statistics','Counsel people with drug or addiction','Create art for sale and exhibition'
]




$('#submit').click(function() {
    $('#question').html(questions.pop());
    $('#options').innerHTML +=`<!--Material Radio-->
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
                                                </label>`
});