package com.example.raviolist;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.android.material.textfield.TextInputEditText;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.FirebaseFirestore;

import java.util.HashMap;
import java.util.Map;

public class RegisterActivity extends AppCompatActivity {
    //UI
    EditText etRegname, etRegemail, etRegpassword, etRegPasswordRepeat;
    TextView tvLoginHere;
    Button btnRegister;

    //Firebase
    FirebaseAuth mAuth;
    FirebaseFirestore fStore;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        //UI
        etRegname = findViewById(R.id.name);
        etRegemail = findViewById(R.id.email);
        etRegpassword = findViewById(R.id.password);
        etRegPasswordRepeat = findViewById(R.id.passwordRepeat);
        tvLoginHere = findViewById(R.id.loginHere);
        btnRegister = findViewById(R.id.registerBtn);

        //Firebase connections
        mAuth = FirebaseAuth.getInstance();
        fStore = FirebaseFirestore.getInstance();

        //Register button triggers registerUser method
        btnRegister.setOnClickListener(view -> {
            createUser();
        });

        //Login link triggers login activity
        tvLoginHere.setOnClickListener(view -> {
            startActivity(new Intent(RegisterActivity.this, LoginActivity.class));
        });
    }

    private void createUser() {
        //Getting user input
        String name = etRegname.getText().toString();
        String email = etRegemail.getText().toString();
        String password = etRegpassword.getText().toString();
        String passwordRepeat = etRegPasswordRepeat.getText().toString();

        //Checking if user input is empty
        if (TextUtils.isEmpty(name)) {
            etRegname.setError("Name is required");
            etRegname.requestFocus();
        }

        else if (TextUtils.isEmpty(email)) {
            etRegemail.setError("Email is required");
            etRegemail.requestFocus();
        }

        else if (TextUtils.isEmpty(password)) {
            etRegpassword.setError("Password is required");
            etRegpassword.requestFocus();
        }

        else if (TextUtils.isEmpty(passwordRepeat)) {
            etRegpassword.setError("Please Repeat Password");
            etRegpassword.requestFocus();
        }

        else if (!password.equals(passwordRepeat)) {
            etRegPasswordRepeat.setError("Passwords do not match");
            etRegPasswordRepeat.requestFocus();
        }

        //If not empty inputs:
        else {
            //Create user in firebase auth
            mAuth.createUserWithEmailAndPassword(email, password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                @Override
                public void onComplete(@NonNull Task<AuthResult> task) {
                    if (task.isSuccessful()) {
                        Toast.makeText(RegisterActivity.this, "User registered Successfully!", Toast.LENGTH_SHORT).show();

                        //Store in Hashmap and send it to Firestore Cloud Database
                        DocumentReference documentReference = fStore.collection("users").document(mAuth.getCurrentUser().getUid());
                        Map<String, Object> user = new HashMap<>();

                        user.put("userID", mAuth.getCurrentUser().getUid());
                        user.put("name", name);
                        user.put("email", email);

                        documentReference.set(user).addOnSuccessListener(new OnSuccessListener<Void>() {
                            @Override
                            public void onSuccess(Void aVoid) {
                                Log.d("TAG", "onSuccess: user profile is created for " + mAuth.getCurrentUser().getUid());

                            }
                        }).addOnFailureListener(new OnFailureListener() {
                            @Override
                            public void onFailure(@NonNull Exception e) {
                                Log.d("TAG", "onFailure: " + e.toString());
                            }
                        });
                        //Send user to login activity
                        startActivity(new Intent(RegisterActivity.this, LoginActivity.class));
                    }
                    //If user creation fails:
                    else {
                        Toast.makeText(RegisterActivity.this, "There was an Error " + task.getException().getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
                }
            );
        }
    }
}