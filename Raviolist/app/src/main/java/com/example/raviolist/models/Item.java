package com.example.raviolist.models;

public class Item {
    private String itemID, itemName, itemCategory, listID;
    private boolean isChecked;

    public Item() {
    }

    public Item(String itemID, String itemName, String itemCategory, String listID, boolean isChecked) {
        this.itemID = itemID;
        this.itemName = itemName;
        this.itemCategory = itemCategory;
        this.listID = listID;
        this.isChecked = isChecked;

    }


    public String getItemID() {
        return itemID;
    }

    public String getItemName() {
        return itemName;
    }

    public String getItemCategory() {
        return itemCategory;
    }

    public String getListID() {
        return listID;
    }

    public boolean getIsChecked() {
        return isChecked;
    }

    public void setItemID(String itemID) {
        this.itemID = itemID;
    }


    public void setItemName(String itemName) {
        this.itemName = itemName;
    }

    public void setItemCategory(String itemCategory) {
        this.itemCategory = itemCategory;
    }

    public void setListID(String listID) {
        this.listID = listID;
    }

    public void setIsChecked(boolean isChecked) {
        this.isChecked = isChecked;
    }



}
