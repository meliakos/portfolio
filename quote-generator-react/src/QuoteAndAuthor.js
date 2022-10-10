import React from "react";

class QuoteAndAuthor extends React.Component {
    render() {
        return (
            
            <div id="container">
                <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous"></link>
                <header>
                    <h1>Inspiring Quotes Generator</h1>
                </header>
                <div id="quote-box">
                    <div>
                        <p id="text">{this.props.quote}</p>
                    </div>
                    <div>
                        <p id="author">~ {this.props.author ? this.props.author : "Unknown"}</p>
                    </div>
                    <div id="buttons">
                        <button id="new-quote" class="btn btn-dark" onClick={this.props.publishQuote}>New Quote</button>
                        <a target="_blank" href="twitter.com/intent/tweet"><button id="tweet-quote" class="btn btn-dark"><i class="fab fa-twitter" aria-label="Tweet Quote"></i></button></a>
                    </div>
                </div>
            </div>
        
        );
    }
}

export default QuoteAndAuthor;