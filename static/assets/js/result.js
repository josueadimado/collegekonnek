let objs = [{img:"/static/assets/img/illustrations/characters/undraw_medical_care_mvn.svg",career:"Nurse"},{img:"/static/assets/img/illustrations/characters/undraw_medical_research_qg4d.svg",career:"Doctor"},{img:"/static/assets/img/illustrations/characters/undraw_product_photography_91i2.svg",career:"Photographer"},{img:"/static/assets/img/illustrations/characters/undraw_business_plan_5i9d.svg",career:"Business Personel"},{img:"/static/assets/img/illustrations/characters/undraw_science_fqhl.svg",career:"Researcher"},{img:"/static/assets/img/illustrations/characters/undraw_medical_research_qg4d.svg",career:"Mathematician"},{img:"/static/assets/img/illustrations/characters/undraw_medical_research_qg4d.svg",career:"Programer"},,{img:"/static/assets/img/illustrations/characters/undraw_medical_research_qg4d.svg",career:"Software Engineer"}]

function random(items){
    return items[Math.floor(Math.random() * items.length)];
}

var selected = random(objs)
console.log(selected)

$('#imageprofession').attr('src',selected.img);
$('#profession').text(selected.career);

