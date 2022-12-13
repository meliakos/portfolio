package com.example.raviolist;

import static com.google.firebase.Timestamp.now;
import static com.google.firebase.firestore.FieldPath.documentId;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;


import androidx.appcompat.app.AppCompatActivity;

import com.example.raviolist.models.List;

import com.google.firebase.Timestamp;
import com.google.firebase.auth.FirebaseAuth;

import com.google.firebase.firestore.DocumentReference;

import com.google.firebase.firestore.FirebaseFirestore;


public class NewListActivity extends AppCompatActivity {

    //Button add, send;
    ImageView back;
    EditText listNameET, listDescET;
    Button cancel, next;
    LinearLayout list;
    Context context;

    // Items to DB
    TextView listName;
    EditText listDesc;

    //Strings for storing
    private String ShoppinglistName;
    private String ShoppinglistDescription;

    private FirebaseFirestore db;
    private FirebaseAuth mAuth;


    //


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_list);

        //DB
        db = FirebaseFirestore.getInstance();
        mAuth = FirebaseAuth.getInstance();

        cancel = findViewById(R.id.cancel_newList);
        listNameET = findViewById(R.id.edtListName);
        listDescET = findViewById(R.id.edtListDesc);
        next = findViewById(R.id.next_newList);
        back = findViewById(R.id.back_viewList);

        context = this;


//////////////////////////////////////////////////////////////////////
        //Adding on click listener to next button
        next.setOnClickListener(v -> {

            //User ID
            String userID = mAuth.getCurrentUser().getUid();


            //Getting the values from the EditTexts
            ShoppinglistName = listNameET.getText().toString().trim();
            ShoppinglistDescription = listDescET.getText().toString().trim();


            //validate not empty
            if (TextUtils.isEmpty(ShoppinglistName)) {
                listNameET.setError("List name is required");
                return;
            } else if (TextUtils.isEmpty(ShoppinglistDescription)) {
                listDescET.setError("List description is required");
                return;
            } else {
                //Add to DB
                addDataToFirestore(ShoppinglistName,ShoppinglistDescription, userID,now());
            }


        });

    //////////////////////////////////////////////////////////////////////

        //Cancel button
        cancel.setOnClickListener(v -> {
            Intent intent = new Intent(NewListActivity.this, HomeActivity.class);
            startActivity(intent);
        });

        //Back button
        back.setOnClickListener(v -> {
            Intent intent = new Intent(NewListActivity.this, HomeActivity.class);
            startActivity(intent);
        });

    }

    //Add to DB //////////////////////////////////////////////////////////////

    private void addDataToFirestore( String ShoppinglistName,String ShoppinglistDescription, String userID, Timestamp now) {

        //Make new document with generated ID
        DocumentReference listRef = db.collection("lists").document();

        //Save List ID to variable
        String listID = listRef.getId();

        //Add to Firestore with generated ID
        listRef.set(new List(listID, ShoppinglistName, ShoppinglistDescription, userID, now)).addOnSuccessListener(documentReference -> {
            Toast.makeText(context, "List added", Toast.LENGTH_SHORT).show();
            //Go to next activity
            Intent intent = new Intent(NewListActivity.this, ViewListActivity.class);
            startActivity(intent);

        }).addOnFailureListener(e -> Toast.makeText(context, "Error adding list", Toast.LENGTH_SHORT).show());;


    }


    //////////////////////////////////////////////////////////////////////


}