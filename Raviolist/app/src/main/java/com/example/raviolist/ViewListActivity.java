package com.example.raviolist;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.AlertDialog;
import android.content.Intent;
import android.content.Context;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ArrayAdapter;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import android.widget.Toast;

import com.example.raviolist.models.Item;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.FirebaseFirestore;

import android.widget.LinearLayout;

import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.Query;
import com.google.firebase.firestore.QueryDocumentSnapshot;

import java.util.concurrent.atomic.AtomicReference;

public class ViewListActivity<TableView> extends AppCompatActivity {

    //UI Components
    TextView listNametv,listDescriptiontv,listName;
    Context context;
    LinearLayout list;
    FloatingActionButton add;
    ImageView back;
    Button btndeleteList;
    Spinner spinner;

    //Firebase
    FirebaseFirestore fStore = FirebaseFirestore.getInstance();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_list);
        String listID = getIntent().getExtras().getString("listID");


        //Initialize UI elements
        listName = findViewById(R.id.txvListName_viewList);

        btndeleteList = findViewById(R.id.deleteList);

        context = this;
        listNametv = findViewById(R.id.txvListName_viewList);
        listDescriptiontv = findViewById(R.id.listDesc_viewList);

        add = findViewById(R.id.FABaddItem);

        //Getting Current listID
        String currentListID = getlistID();

        //Set textviews
        listNametv.setText(getlistName());
        listDescriptiontv.setText(getlistDescription());

        btndeleteList.setOnClickListener(v -> deleteList(currentListID));

        ////////////////////

        //Get info from Firebase
        back = findViewById(R.id.back_viewList);
        list = findViewById(R.id.viewList);

        //send button back to home
        back.setOnClickListener(v -> finish());


        //Add item to list
        add.setOnClickListener(v -> addItem(currentListID));

        //Spinner
        spinner = findViewById(R.id.spinner);



        //Initialiing the spinner
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.sortBy, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        //Spinner listener
        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                String selected = parent.getItemAtPosition(position).toString();
                //Clear the list

                getItems(currentListID,selected);


            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
                String selected = parent.getItemAtPosition(0).toString();
                //Clear the list

                getItems(currentListID,selected);

            }
        });

        //getItems(currentListID,"Sort by:");

    }


    
    //Method to update firestore when checkbox is checked
    public void updateItem(String listID, String itemID, boolean isChecked) {
        //Update item in firestore
        DocumentReference docRef = fStore.collection("items").document(itemID);
        docRef.update("isChecked", isChecked);

        //Refresh list
        finish();
        startActivity(getIntent());

    }

    //Method to delete item from firestore
    public void deleteItem(String itemID) {
        //Adding a new Dialog
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle(getString(R.string.delete_item_dialog));
        builder.setMessage(getString(R.string.delete_item_dialog_text));
        //Setting positive button
        builder.setPositiveButton(getString(R.string.delete_item_dialog_delete), (dialog, which) -> {
            //Delete item from firestore
            DocumentReference docRef = fStore.collection("items").document(itemID);
            docRef.delete();
                    Toast.makeText(context, "Item deleted", Toast.LENGTH_SHORT).show();
                    finish();
                    startActivity(getIntent());
                });
        //Setting negative button
        builder.setNegativeButton(getString(R.string.delete_item_dialog_cancel), (dialog, which) -> dialog.cancel());

        builder.show();
    }



    //Method to get all items in the list based on query
    public void getItems(String listID, String selected) {

        //Initializing the tablelayout
        TableLayout tableLayout = findViewById(R.id.listItemstl);
        tableLayout.removeAllViews();

        //Collection reference to firebase
        CollectionReference items = fStore.collection("items");

        //Query to get items from firestore
        Query query = items.whereEqualTo("listID", listID);

        //Query to sort items
        if (selected.equals("Sort by:")) {
            query = query.orderBy("isChecked", Query.Direction.ASCENDING);
        } else if (selected.equals("Category A-Z")) {
            query = query.orderBy("itemCategory", Query.Direction.ASCENDING);
        } else if (selected.equals("Category Z-A")) {
            query = query.orderBy("itemCategory", Query.Direction.DESCENDING);
        } else if (selected.equals("Item A-Z")) {
            query = query.orderBy("itemName", Query.Direction.ASCENDING);
        } else if (selected.equals("Item Z-A")) {
            query = query.orderBy("itemName", Query.Direction.DESCENDING);
        } else if (selected.equals("Finished")) {
            query = query.orderBy("isChecked", Query.Direction.ASCENDING);
        } else
            query = query.orderBy("isChecked", Query.Direction.ASCENDING);

        //Getting the items from firestore
        query.get().addOnSuccessListener(queryDocumentSnapshots -> {
            for (QueryDocumentSnapshot documentSnapshot : queryDocumentSnapshots) {
                Item item = documentSnapshot.toObject(Item.class);
                String itemID = documentSnapshot.getId();
                String name = item.getItemName();
                String category = item.getItemCategory();
                boolean checked = item.getIsChecked();

                //Creating a new row for each item
                TableRow tableRow = new TableRow(this);
                tableRow.setLayoutParams(new TableRow.LayoutParams(TableRow.LayoutParams.MATCH_PARENT, TableRow.LayoutParams.WRAP_CONTENT));
                tableRow.setPadding(0, 1, 3, 0);

                //Create textview for item name
                TextView tvName = new TextView(this);
                tvName.setLayoutParams(new TableRow.LayoutParams(TableRow.LayoutParams.WRAP_CONTENT, TableRow.LayoutParams.WRAP_CONTENT));
                tvName.setPadding(10, 0, 0, 0);
                tvName.setTextSize(20);
                tvName.setWidth(400);

                //Setting the item name
                tvName.setText(name);

                //Create textview for item category
                TextView tvCat = new TextView(this);
                tvCat.setLayoutParams(new TableRow.LayoutParams(TableRow.LayoutParams.WRAP_CONTENT, TableRow.LayoutParams.WRAP_CONTENT));
                tvCat.setPadding(0, 0, 0, 0);
                tvCat.setTextSize(20);
                tvCat.setTextColor(Color.parseColor("#6DBC94"));

                //Setting the item category
                tvCat.setText(category);

                //Create checkbox
                CheckBox cb = new CheckBox(this);
                cb.setLayoutParams(new TableRow.LayoutParams(TableRow.LayoutParams.WRAP_CONTENT, TableRow.LayoutParams.WRAP_CONTENT));
                cb.setPadding(0, 0, 0, 0);
                cb.setTextColor(Color.parseColor("#B0EACD"));

                //Setting the checkbox to unchecked
                cb.setChecked(checked);

                //Adding textviews and checkbox to row
                tableRow.addView(cb);
                tableRow.addView(tvName);
                tableRow.addView(tvCat);

                //Adding row to table
                tableLayout.addView(tableRow);

                //When checkbox is clicked
                cb.setOnClickListener(v -> updateItem(listID, itemID, cb.isChecked()));

                //When row is long clicked
                tableRow.setOnLongClickListener(v -> {
                    //Delete item
                    deleteItem(itemID);

                    return true;
                });

            }
        });

    }

    //Add item to list
    private void addItem(String currentListID) {

            //Create dialog
            AlertDialog.Builder builder = new AlertDialog.Builder(this);
            builder.setTitle(getString(R.string.add_item_dialog));

            //Create layout for dialog
            LinearLayout layout = new LinearLayout(this);
            layout.setOrientation(LinearLayout.VERTICAL);
            layout.setPadding(20, 10, 20, 10);

            //Create edit text for item name
            EditText itemName = new EditText(this);
            itemName.setHint(getString(R.string.add_item_dialog_hint));
            itemName.setLayoutParams(new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));
            layout.addView(itemName);

            //Create spinner for item category
            Spinner category = new Spinner(this);
            ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.categories, android.R.layout.simple_spinner_item);
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
            category.setAdapter(adapter);
            category.setLayoutParams(new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT));
            layout.addView(category);

            //Add layout to dialog
            builder.setView(layout);

            //Add buttons to dialog
            builder.setPositiveButton(getString(R.string.add_item_dialog_add), (dialog, which) -> {
                //Get item name and quantity
                String name = itemName.getText().toString();
                String cat = category.getSelectedItem().toString();

                //Add item to collection
                DocumentReference docRef = fStore.collection("items").document();
                docRef.set(new Item(docRef.getId(),name,cat,currentListID,false)).addOnSuccessListener(aVoid -> {
                    Log.d("TAG", "Item added to list" + name);
                    Toast.makeText(ViewListActivity.this, "Item added", Toast.LENGTH_SHORT).show();
                    finish();
                    startActivity(getIntent());
                }).addOnFailureListener(e -> Toast.makeText(ViewListActivity.this, "Error adding item", Toast.LENGTH_SHORT).show());

            });

            //Cancel button
            builder.setNegativeButton(getString(R.string.add_item_dialog_cancel), (dialog, which) -> dialog.cancel());

            //Show dialog
            builder.show();
    }

    //Method to delete List
    private void deleteList(String currentListID) {
        //Create dialog
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle(getString(R.string.delete_list_dialog))
        .setMessage(getString(R.string.delete_list_dialog_text));

        //Add buttons to dialog
        builder.setPositiveButton(getString(R.string.delete_item_dialog_delete), (dialog, which) -> {
            //Delete list from collection
            //Get list id

            fStore.collection("lists").document(currentListID).delete().addOnSuccessListener(aVoid -> {
                Log.d("TAG", "List deleted");
                Log.d("TAG", "List ID: " + currentListID);
                Toast.makeText(ViewListActivity.this, "List deleted", Toast.LENGTH_SHORT).show();
                finish();
            }).addOnFailureListener(e -> Toast.makeText(ViewListActivity.this, "Error deleting list", Toast.LENGTH_SHORT).show());
        });

        //Cancel button
        builder.setNegativeButton(getString(R.string.delete_item_dialog_cancel), (dialog, which) -> dialog.cancel());

        //Show dialog
        builder.show();
    }


    private String getlistName() {
        String listName = getIntent().getStringExtra("listName");
        return listName;
    }

    private String getlistID() {
        //Get list ID with list name
        String listID = getIntent().getStringExtra("listID");
        return listID;
    }

    private String getlistDescription() {
        String listDescription = getIntent().getStringExtra("listDescription");
        return listDescription;
    }




}