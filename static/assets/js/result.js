let objs = [{img:"/static/assets/img/illustrations/characters/crowd.svg",career:"Nurse"},{img:"/static/assets/img/illustrations/characters/crowd.svg",career:"Doctor"}]

function random(items){
    return items[Math.floor(Math.random() * items.length)];
}

var selected = random(objs)
console.log(selected)

$('#imageprofession').attr('src',selected.img);
$('#profession').text(selected.career);

