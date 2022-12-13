package com.example.raviolist;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.EventListener;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;
import com.google.firebase.firestore.Query;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;
import java.util.ArrayList;
import java.util.List;


public class HomeFragment extends Fragment {

    //Firebase
    FirebaseFirestore fStore = FirebaseFirestore.getInstance();
    FirebaseAuth mAuth = FirebaseAuth.getInstance();

    //Current user
    String userID = mAuth.getCurrentUser().getUid();


    //UI elements
    TextView tvSetUserName;

    ListView lvListNames;

    Context context;



    public HomeFragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_home, container, false);
        FloatingActionButton fab = view.findViewById(R.id.fab_newList);


        //Adding user name to the home screen
        tvSetUserName = view.findViewById(R.id.tvUserName);
        setName();

        //set context
        context = view.getContext();

        //Get the listview
        lvListNames = view.findViewById(R.id.listNames);

        //Set the listview
        getListNamesList();

        //Add new list
        fab.setOnClickListener(v -> {
            Intent intent = new Intent(getActivity(), NewListActivity.class);
            startActivity(intent);
        });
        return view;

    }
    //Method to get the users name from the database
    public void setName(){
        //Get the user name from the database
        DocumentReference documentReference = fStore.collection("users").document(userID);
        documentReference.get().addOnSuccessListener(new OnSuccessListener<DocumentSnapshot>() {
            @Override
            public void onSuccess(DocumentSnapshot documentSnapshot) {
                if (documentSnapshot.exists()) {
                    tvSetUserName.setText(documentSnapshot.getString("name"));
                } else {
                    Log.d("TAG", "onSuccess: Document does not exist");
                }
            }
        });

    }

    //Method to get all the list names from the database
    public void getListNamesList(){
        //Get the list of all the lists
        CollectionReference collectionReference = fStore.collection("lists");

        //Get the list of all the list names
        collectionReference.whereEqualTo("createdBy", userID).orderBy("dateCreated", Query.Direction.DESCENDING).addSnapshotListener(new EventListener<QuerySnapshot>() {
            @Override
            public void onEvent(@Nullable QuerySnapshot value, @Nullable FirebaseFirestoreException error) {
                if (error != null) {
                    Log.d("TAG", "onEvent: Error: " + error.getMessage());
                    return;
                }

                //Get the list of all the list names
                List<String> listNames = new ArrayList<>();
                //And a list with the list ids
                List<String> listIds = new ArrayList<>();
                for (QueryDocumentSnapshot documentSnapshot : value) {
                    //Adding list name to the listview
                    listNames.add(documentSnapshot.getString("listName"));
                    //Adding list list info to list of list ids
                    listIds.add(documentSnapshot.getId());
                    listIds.add(documentSnapshot.getString("listName"));
                    listIds.add(documentSnapshot.getString("description"));

                }

                //Set the list of all the list names to the listview
                ArrayAdapter<String> arrayAdapter = new ArrayAdapter<>(context, android.R.layout.simple_list_item_1, listNames);
                lvListNames.setAdapter(arrayAdapter);

                //Adding click listener to the listview
                lvListNames.setOnItemClickListener((parent, view, position, id) -> {

                    Intent intent = new Intent(getActivity(), ViewListActivity.class);

                    //Passing the list id to the next activity
                    intent.putExtra("listName", listNames.get(position));

                    //Find the list id matching the name in the list of ids
                    int listIdIndex = listIds.indexOf(listNames.get(position));

                    //Get the matching list id and description
                    String listId = listIds.get(listIdIndex - 1);
                    String listDescription = listIds.get(listIdIndex + 1);

                    //Passing the list id and description to the next activity
                    intent.putExtra("listID", listId);
                    intent.putExtra("listDescription", listDescription);
                    startActivity(intent);
                });

            }
        });
    }


}
