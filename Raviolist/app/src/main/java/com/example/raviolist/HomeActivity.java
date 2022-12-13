package com.example.raviolist;

import static android.content.ContentValues.TAG;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.android.material.bottomnavigation.BottomNavigationView;


public class HomeActivity extends AppCompatActivity {

    BottomNavigationView bottomNavigationView;
    HomeFragment home_Fragment = new HomeFragment();
    SettingsFragment settings_Fragment = new SettingsFragment();
    private boolean isBackPressedOnce = false;
    EditText etToken;

    @SuppressLint("NonConstantResourceId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);


        //NAV BAR
        bottomNavigationView = findViewById(R.id.bottomNavigationView);

        getSupportFragmentManager().beginTransaction().replace(R.id.fragmentContainerView,home_Fragment).commit();
        bottomNavigationView.setOnItemSelectedListener(item -> {

            switch (item.getItemId()){
                case R.id.homeFragment:
                    getSupportFragmentManager().beginTransaction().replace(R.id.fragmentContainerView,home_Fragment).commit();
                    return true;
                case R.id.settingsFragment:
                    getSupportFragmentManager().beginTransaction().replace(R.id.fragmentContainerView,settings_Fragment).commit();
                    return true;
            }
            return false;
        });

    }


    //Double back press to exit
    public void onBackPressed() {
        if (isBackPressedOnce) {
            super.onBackPressed();
            return;
        }
        isBackPressedOnce = true;
        Toast.makeText(this, "Press back again to exit", Toast.LENGTH_SHORT).show();

        new Handler().postDelayed(() -> isBackPressedOnce = false, 2000);
    }



}
