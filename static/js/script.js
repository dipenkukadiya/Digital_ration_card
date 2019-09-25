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
        set_attribute(aadhaar, { "type": "text",  "class": "form-control", "placeholder": " Aadhaar Number", "name" : "aadhaar_"+i});
        document.getElementById("fam_members").appendChild(aadhaar); 

        var f_name = document.createElement("input");
        set_attribute(f_name, { "type": "text", "class": "form-control", "placeholder": " Full Name", "name" : "f_name_"+i});
        document.getElementById("fam_members").appendChild(f_name);

        var relation = document.createElement("input");
        set_attribute(relation, { "type": "text", "class": "form-control", "placeholder": "your relationship", "name" : "relation_"+i});
        document.getElementById("fam_members").appendChild(relation);

        var age = document.createElement("input");
        set_attribute(age, { "type": "number", "class": "form-control", "placeholder": "Age ", "name" : "age_"+i});
        document.getElementById("fam_members").appendChild(age);

        var gender = document.createElement("input");
        set_attribute(gender, { "type": "text", "class": "form-control", "placeholder": "Gender", "name" : "gender_"+i});
        document.getElementById("fam_members").appendChild(gender);





        console.log(dd_value);
        if(i == dd_value)
        {
            $modal = $('#modalFamily');
            $modal.modal('show');
        }
    }

    var but = document.createElement("input");
    set_attribute(but, { "type":"button","class": "form-control" , "name":"submit ","value":"submit", "id" : "but"});
    document.getElementById("fam_members").appendChild(but);
}

function set_attribute(elem, attrs)
{
    for(var key in attrs)
    {
        elem.setAttribute(key, attrs[key]);
    }
}
