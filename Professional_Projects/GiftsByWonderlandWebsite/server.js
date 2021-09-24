if (process.env.NODE_ENV !== "production") {
    require("dotenv").config()
}


const stripeSecretKey = process.env.STRIPE_SECRET_KEY
const stripePublicKey = process.env.STRIPE_PUBLIC_KEY


const express = require("express")
const app = express()
const fs = require("fs")
const stripe = require("stripe")(stripeSecretKey)

app.set("view engine", "ejs") 
app.use(express.json())
app.use(express.static("public"))


app.get("/shopping_cart", function(req, res) {
    fs.readFile("items.json", function(error, data) {
        if (error) {
            res.status(500).end()
        } else {
            res.render("shopping_cart.ejs", {
                stripePublicKey: stripePublicKey, 
                items: JSON.parse(data)

            })
        }
    })
})

app.post("/purchase", function(req, res) {
    fs.readFile("items.json", function(error, data) {
        if (error) {
            res.status(500).end()
        } else {
            const itemsJson = JSON.parse(data)
            const itemsArray = itemsJson.store_items
            let total = 0 
            console.log(req.body.items)
            req.body.items.forEach(function(item) {
                const itemJson = itemsArray.find(function(i) {
                    return i.title == item.title
            
                })
                total = total + (itemJson.price * item.quantity)
            })
            stripe.charges.create({
                amount: total,
                source: req.body.stripeTokenId,
                currency: "usd"
            }).then(function() {

                console.log("charge successfull")
                res.json({message: "successfully purchased items"})
            }).catch(function() {
                console.log("charge fail")
                res.status(500).end()
            })

        }
    })
})


app.listen(3000)
