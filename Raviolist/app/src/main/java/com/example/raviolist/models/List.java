package com.example.raviolist.models;

import com.google.firebase.Timestamp;
import com.google.firebase.firestore.ServerTimestamp;

import java.util.ArrayList;
import java.util.Date;

public class List {

    private String listName,description,createdBy, listID;
    @ServerTimestamp
    private Timestamp dateCreated;


    public List(String listID,String listName, String description, String createdBy, Timestamp dateCreated) {
        this.listID = listID;
        this.listName = listName;
        this.description = description;
        this.createdBy = createdBy;
        this.dateCreated = dateCreated;

    }

    public String getListID() {
        return listID;
    }

    public void setListID(String listID) {
        this.listID = listID;
    }

    public String getListName() {
        return listName;
    }

    public void setListName(String listName) {
        this.listName = listName;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getCreatedBy() {
        return createdBy;
    }

    public void setCreatedBy(String createdBy) {
        this.createdBy = createdBy;
    }


    public Timestamp getDateCreated() {
        return dateCreated;
    }

    public void setDateCreated(Timestamp dateCreated) {
        this.dateCreated = dateCreated;
    }






}
