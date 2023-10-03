function func1() {
    document.getElementById("modalFamily").style.display = "block";
    var i;
    var dd_value = document.getElementById("sel").value;

    var e = document.getElementById("fam_members");
    e.innerHTML = "";

    
    window.set_attribute = function(elem, attrs) {
        for (var key in attrs) {
            elem.setAttribute(key, attrs[key]);
        }
    }

    for (i = 1; i <= dd_value; i++) {

        //document.getElementById("fam_members").appendChild(document.createElement("br"));

        var aadhaar = document.createElement("input");
        set_attribute(aadhaar, { "type": "text", "class": "form-control", "pattern" :"^\d{4}\d{4}\d{4}$","placeholder": " Aadhaar Number", "name": "aadhaar_" + i, "minlength":"12", "maxlength":"12" }) ;
        document.getElementById("fam_members").appendChild(aadhaar);

        var f_name = document.createElement("input");
        set_attribute(f_name, { "type": "text", "class": "form-control", "placeholder": " Full Name","pattern" :"[a-zA-Z]{1,}", "name": "f_name_" + i });
        document.getElementById("fam_members").appendChild(f_name);

        var relation = document.createElement("input");
        set_attribute(relation, { "type": "text", "class": "form-control", "placeholder": "your relationship","pattern" :"[a-zA-Z]{1,}", "name": "relation_" + i });
        document.getElementById("fam_members").appendChild(relation);

        var age = document.createElement("input");
        set_attribute(age, { "type": "text", "class": "form-control", "placeholder": "Age ","minlength":"3", "maxlength":"3","pattern":"[0-9]{3}" ,"name": "age_" + i });
        document.getElementById("fam_members").appendChild(age);

        var gender = document.createElement("input");
        set_attribute(gender, { "type": "text", "class": "form-control", "placeholder": "Gender","pattern" :"[a-zA-Z]{1,}", "name": "gender_" + i });
        document.getElementById("fam_members").appendChild(gender);



        console.log("checkpoint...");

        console.log(dd_value);
        if (i == dd_value) {
            $modal = $('#modalFamily');
            $modal.modal('show');
        }
    }

    var but = document.createElement("input");
    set_attribute(but, { "type": "button", "class": "form-control", "name": "submit ", "value": "submit", "id": "but", "onclick": "asap()" } );
    document.getElementById("fam_members").appendChild(but);
    console.log(but);
    console.log("check............. 2...........");


// Add the following code if you want the name of the file appear on select

}

function asap() {
    console.log("checkpoint...2");
    var dd_value = document.getElementById("sel").value;
    console.log("ankitdsd");
    
    for (i = 1; i <= dd_value; i++) {
        var aadhaar = document.getElementsByName("aadhaar_"+i)[0].value;
        var f_name = document.getElementsByName("f_name_"+i)[0].value;
        var age = document.getElementsByName("age_"+i)[0].value;
        var gender = document.getElementsByName("gender_"+i)[0].value;
        var relation = document.getElementsByName("relation_"+i)[0].value;

    
        var node = document.createElement("input");

        var data = {
            "aadhaar":aadhaar,
            "f_name":f_name,
            "age":age,
            "gender":gender,
            "relation":relation
        };
        
        set_attribute(node, {"type": "hidden", "value": JSON.stringify(data), "name" : "family_"+i});
        document.getElementById("regis").appendChild(node);
        
    }
    var nodee = document.createElement("input");
    set_attribute(nodee, {"type" : "hidden" ,"data-value" : dd_value ,"name" : "select"}) ;
    document.getElementById("regis").appendChild(nodee);
    console.log("................................//....................");
    document.getElementById("modalFamily").style.display = "none";
 
} 
