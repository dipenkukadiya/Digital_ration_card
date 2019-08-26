function func1()
{
    var i;
    var dd_value = document.getElementById("sel").value;

    var e = document.getElementById("fam_members");
    e.innerHTML = "";


    for (i = 1; i <= dd_value; i++)
    {

        //document.getElementById("fam_members").appendChild(document.createElement("br"));

        var aadhaar = document.createElement("input");
        set_attribute(aadhaar, { "type": "text", "class": "form-control mb-2 mr-sm-2", "placeholder": "Enter your Aadhaar Number:", "name" : "aadhaar_"+i});
        document.getElementById("fam_members").appendChild(aadhaar);

        var f_name = document.createElement("input");
        set_attribute(f_name, { "type": "text", "class": "form-control mb-2 mr-sm", "placeholder": "Enter your Full Name", "name" : "f_name_"+i});
        document.getElementById("fam_members").appendChild(f_name);

        var relation = document.createElement("input");
        set_attribute(relation, { "type": "text", "class": "form-control mb-2 mr-sm-2", "placeholder": "Enter your relationship", "name" : "relation_"+i});
        document.getElementById("fam_members").appendChild(relation);

        var age = document.createElement("input");
        set_attribute(age, { "type": "number", "class": "form-control mb-2 mr-sm-2", "placeholder": "How old are you?", "name" : "age_"+i});
        document.getElementById("fam_members").appendChild(age);

        var dob = document.createElement("input");
        set_attribute(dob, { "type": "date", "class": "form-control mb-2 mr-sm-2", "placeholder": "Enter your Date of Birth", "name" : "dob_"+i});
        document.getElementById("fam_members").appendChild(dob);

        var gender = document.createElement("input");
        set_attribute(gender, { "type": "text", "class": "form-control mb-2 mr-sm-2", "placeholder": "Gender", "name" : "gender_"+i});
        document.getElementById("fam_members").appendChild(gender);


        console.log(dd_value);
        if(i == dd_value)
        {
            $modal = $('#modalFamily');
            $modal.modal('show');
        }
    }
}

function set_attribute(elem, attrs)
{
    for(var key in attrs)
    {
        elem.setAttribute(key, attrs[key]);
    }
}
