package com.example.raviolist;

import android.app.AlertDialog;
import android.content.Context;
import android.content.Intent;

import android.os.Bundle;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.Spinner;
import android.widget.Switch;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.messaging.FirebaseMessaging;

import java.util.Locale;


public class SettingsFragment extends Fragment {


    private FirebaseAuth mAuth = FirebaseAuth.getInstance();

    FirebaseUser user = mAuth.getCurrentUser();


    Switch switchNotifications;



    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    public SettingsFragment() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {

            getArguments().getString(ARG_PARAM1);
            getArguments().getString(ARG_PARAM2);
        }




    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_settings, container, false);


        mAuth = FirebaseAuth.getInstance();

        switchNotifications = view.findViewById(R.id.switch1);

        switchNotifications.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    // Subscribe the user to a Firebase messaging topic
                    FirebaseMessaging.getInstance().subscribeToTopic("notifications");
                    Toast.makeText(getContext(), "Notifications enabled", Toast.LENGTH_SHORT).show();
                } else {
                    // Unsubscribe the user from the topic
                    FirebaseMessaging.getInstance().unsubscribeFromTopic("notifications");
                    Toast.makeText(getContext(), "Notifications disabled", Toast.LENGTH_SHORT).show();
                }
            }
        });




        Button logOutBtn = view.findViewById(R.id.logOutBtn);

        logOutBtn.setOnClickListener(view1 -> {
            new AlertDialog.Builder(getActivity())
                    .setTitle(R.string.logout_popup_title)
                    .setMessage(R.string.logout_popup)
                    .setPositiveButton(R.string.logout_popup_yes, (dialogInterface, i) -> {
                        mAuth.signOut();
                        startActivity(new Intent(getActivity(), LoginActivity.class));
                        Toast.makeText(getActivity(), R.string.logout_popup_toast, Toast.LENGTH_SHORT).show();
                    })
                    .setNegativeButton(R.string.logout_popup_no, null)
                    .show();
            mAuth.signOut();

        });


        //Delete user
        Button deleteBtn = view.findViewById(R.id.delete_account_button);
        deleteBtn.setOnClickListener(view1 -> {
            new AlertDialog.Builder(getActivity())
                    .setTitle(R.string.delete_popup_title)
                    .setMessage(R.string.delete_popup)
                    .setPositiveButton(R.string.delete_popup_yes, (dialogInterface, i) -> {

                        user.delete()
                                .addOnCompleteListener(new OnCompleteListener<Void>() {
                                    @Override
                                    public void onComplete(@NonNull Task<Void> task) {
                                        if (task.isSuccessful()) {
                                            Log.d("TAG", "User account deleted.");
                                            startActivity(new Intent(SettingsFragment.this.getActivity(), LoginActivity.class));
                                            Toast.makeText(getActivity(), R.string.delete_popup_toast, Toast.LENGTH_SHORT).show();

                                        }
                                    }
                                });
                    })
                    .setNegativeButton(R.string.delete_popup_no, null)
                    .show();
            mAuth.signOut();

        });

        return view;
    }


}
