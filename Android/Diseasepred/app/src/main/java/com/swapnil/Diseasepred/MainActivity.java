package com.swapnil.Diseasepred;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    Spinner s1,s2,s3,s4,s5;
    Button predict;
    TextView test;
    String url = "http://axelblaze26.pythonanywhere.com/";
    static String[] symptoms= new String[]{"abdominal_pain", "abnormal_menstruation", "acute_liver_failure", "altered_sensorium",
            "back_pain", "belly_pain", "blackheads", "blister", "bloody_stool", "blurred_and_distorted_vision",
            "bruising", "burning_micturition", "chest_pain", "coma", "congestion", "constipation",
            "continuous_feel_of_urine", "cough", "cramps", "dark_urine", "dehydration", "depression",
            "diarrhoea", "dischromic _patches", "distention_of_abdomen", "dizziness", "drying_and_tingling_lips",
            "enlarged_thyroid", "excessive_hunger", "extra_marital_contacts", "family_history",
            "fast_heart_rate", "fatigue", "fluid_overload", "foul_smell_of urine", "headache", "high_fever",
            "hip_joint_pain", "history_of_alcohol_consumption", "increased_appetite", "indigestion",
            "inflammatory_nails", "internal_itching", "irregular_sugar_level", "irritability",
            "irritation_in_anus", "joint_pain", "knee_pain", "lack_of_concentration", "lethargy",
            "loss_of_appetite", "loss_of_balance", "loss_of_smell", "malaise", "mild_fever",
            "mood_swings", "movement_stiffness", "mucoid_sputum", "muscle_pain", "muscle_weakness",
            "neck_pain", "nodal_skin_eruptions", "obesity", "pain_behind_the_eyes",
            "pain_during_bowel_movements", "pain_in_anal_region", "painful_walking",
            "palpitations", "passage_of_gases", "patches_in_throat", "phlegm", "polyuria",
            "prominent_veins_on_calf", "puffy_face_and_eyes", "pus_filled_pimples", "red_sore_around_nose",
            "red_spots_over_body", "redness_of_eyes", "receiving_blood_transfusion",
            "receiving_unsterile_injections", "regurgitation", "restlessness", "rusty_sputum",
            "scurring", "shivering", "silver_like_dusting", "sinus_pressure", "skin_peeling",
            "skin_rash", "slurred_speech", "small_dents_in_nails", "spinning_movements", "spotting_ urination",
            "stiff_neck", "stomach_bleeding", "stomach_pain", "sunken_eyes", "sweating", "swelled_lymph_nodes",
            "swelling_joints", "swelling_of_stomach", "swollen_blood_vessels", "swollen_extremeties",
            "swollen_legs", "throat_irritation", "toxic_look_(typhos)", "ulcers_on_tongue",
            "unsteadiness", "visual_disturbances", "vomiting", "watering_from_eyes", "weakness_in_limbs",
            "weight_gain","weight_loss","yellow_crust_ooze","yellow_urine", "yellowing_of_eyes"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Spinner s1 = findViewById(R.id.s1);
        Spinner s2 = findViewById(R.id.s2);
        Spinner s3 = findViewById(R.id.s3);
        Spinner s4 = findViewById(R.id.s4);
        Spinner s5= findViewById(R.id.s5);
        predict = findViewById(R.id.predict);

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, symptoms);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        s1.setAdapter(adapter);

        ArrayAdapter<String> adapter2 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, symptoms);
        adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        s2.setAdapter(adapter2);

        ArrayAdapter<String> adapter3 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, symptoms);
        adapter3.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        s3.setAdapter(adapter3);

        ArrayAdapter<String> adapter4 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, symptoms);
        adapter4.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        s4.setAdapter(adapter4);

        ArrayAdapter<String> adapter5 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, symptoms);
        adapter5.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        s5.setAdapter(adapter5);

        predict.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                StringRequest stringrequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        try {
                            JSONObject jsonObject = new JSONObject(response);
                            String data = jsonObject.getString("disease");
                            JSONObject infobject =jsonObject.getJSONObject("info");
                            String intro = infobject.getString("introduction");
                            String prec = infobject.getString("precautions");
                            AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
                            // Set the message show for the Alert time
                            builder.setMessage("Introduction: " +intro+ "\n"+"\n"+"Precautions: "+prec);

                            // Set Alert Title
                            builder.setTitle("Prognosis: "+data);

                            // Set Cancelable false for when the user clicks on the outside the Dialog Box then it will remain show
                            builder.setCancelable(false);

                            // Set the positive button with yes name Lambda OnClickListener method is use of DialogInterface interface.
                            builder.setPositiveButton("ok", (DialogInterface.OnClickListener) (dialog, which) -> {
                                // When the user click yes button then app will close
                            });


                            // Create the Alert dialog
                            AlertDialog alertDialog = builder.create();
                            // Show the Alert Dialog box
                            alertDialog.show();



                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(MainActivity.this, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }){
                    @Override
                    protected Map<String, String> getParams() {
                        Map<String,String> params = new HashMap<String,String>();
                        params.put("s1",s1.getSelectedItem().toString());
                        params.put("s2",s2.getSelectedItem().toString());
                        params.put("s3",s3.getSelectedItem().toString());
                        params.put("s4",s4.getSelectedItem().toString());
                        params.put("s5",s5.getSelectedItem().toString());
                        return params;
                    }
                };
                RequestQueue queue = Volley.newRequestQueue(MainActivity.this);
                queue.add(stringrequest);
            }
        });

    }
    @Override
    public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
        Toast.makeText(this,"Hi",Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }


}