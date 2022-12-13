package com.example.raviolist.models;

public class User {

    private static String name;
    private String email;
    private String userID;

    public User() {

    }

    public User(String email, String password, String name, String userID) {
        this.email = email;
        this.name = name;
        this.userID = userID;
    }

    public User(String name, String userID) {
        this.name = name;
        this.userID = userID;
    }

    public static String getName() {
        return name;
    }


    public String getEmail() {
        return email;
    }

    public String getUserID() {
        return userID;
    }

    public void setName(String name) {
        this.name = name;
    }


    public void setEmail(String email) {
        this.email = email;
    }

    public void setUserID(String userID) {
        this.userID = userID;
    }
}
