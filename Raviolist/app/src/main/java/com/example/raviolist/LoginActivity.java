package com.example.raviolist;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.firestore.FirebaseFirestore;

public class LoginActivity extends AppCompatActivity {
    //UI
    EditText etLoginEmail, etLoginPassword;
    TextView tvRegisterHere, tvForgotPassword;
    Button btnLogin;

    //Firebase
    FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        //UI
        etLoginEmail = findViewById(R.id.email);
        etLoginPassword = findViewById(R.id.password);
        tvRegisterHere = findViewById(R.id.registerHere);
        tvForgotPassword = findViewById(R.id.forgotPassword);
        btnLogin = findViewById(R.id.loginBtn);

        //Firebase connection to auth
        mAuth = FirebaseAuth.getInstance();

        //Login button triggers loginUser method
        btnLogin.setOnClickListener(view -> loginUser());

        //Register link triggers register activity
        tvRegisterHere.setOnClickListener(view -> startActivity(new Intent(LoginActivity.this, RegisterActivity.class)));


        //Forgot password link triggers password reset activity
        tvForgotPassword.setOnClickListener(view -> {

            EditText resetMail = new EditText(view.getContext());
            AlertDialog.Builder passwordResetDialog = new AlertDialog.Builder(view.getContext());
            passwordResetDialog.setTitle("Reset Password?");
            passwordResetDialog.setMessage("Enter your email to receive reset link.");
            passwordResetDialog.setView(resetMail);

            passwordResetDialog.setPositiveButton("Send me a link", (dialog, which) -> {

                //extract the email and send reset link
                String mail = resetMail.getText().toString();

                //Firebase connection to auth and send reset link
                mAuth.sendPasswordResetEmail(mail).addOnSuccessListener(aVoid -> Toast.makeText(LoginActivity.this, "Reset Link Sent to your Email.", Toast.LENGTH_SHORT).show()).addOnFailureListener(e -> Toast.makeText(LoginActivity.this, "Error! Could not send Reset Link" + e.getMessage(), Toast.LENGTH_SHORT).show());
            });

            passwordResetDialog.setNegativeButton("Cancel", (dialogInterface, i) -> {
                //close the dialog
            });


            passwordResetDialog.create().show();
        });


    }

    //Login user method
    private void loginUser() {

        //Get email and password from UI
        String email = etLoginEmail.getText().toString();
        String password = etLoginPassword.getText().toString();

        //Check if email and password are empty
        if (TextUtils.isEmpty(email)) {
            etLoginEmail.setError("Email cannot be empty");
            etLoginEmail.requestFocus();
        }

        else if (TextUtils.isEmpty(password)) {
            etLoginPassword.setError("Password cannot be empty");
            etLoginPassword.requestFocus();
        }

        //If email and password are not empty, try login
        else {
            mAuth.signInWithEmailAndPassword(email, password).addOnCompleteListener(task -> {
                if (task.isSuccessful()) {
                    Toast.makeText(LoginActivity.this, "Login successful", Toast.LENGTH_SHORT).show();

                    //If login is successful, save user
                    String currentUserEmail = mAuth.getCurrentUser().getEmail();


                    //Send user to main activity
                    Intent i = new Intent(LoginActivity.this, HomeActivity.class);
                    startActivity(i);

                }
                //If login fails, show error message
                else {
                    Toast.makeText(LoginActivity.this, "Login failed", Toast.LENGTH_SHORT).show();
                }
            });
        }
    }

    //Check if user is already logged in
    @Override
    protected void onStart() {
        super.onStart();
        FirebaseUser user = mAuth.getCurrentUser();
        if (user != null) {
            // User is signed in
            startActivity(new Intent(LoginActivity.this, HomeActivity.class));
            finish();
        }
    }


}