import './custom.scss';
import React from 'react';
import quotes from './QuotesDatabase'
import QuoteAndAuthor from "./QuoteAndAuthor";

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      quote: quotes[0].quote,
      author: quotes[0].author,
    };
  }

  refreshQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
  }

  shuffleQuotes(array) {
    return array.sort(() => Math.random() - 0.5);
  }

  publishQuote = () => {
    const randomQuote = this.refreshQuote();
    this.setState({
      quote: randomQuote.quote,
      author: randomQuote.author,
    });
    this.shuffleQuotes(quotes);
  };

  render() {
    return (
      <div>
        <QuoteAndAuthor
          publishQuote={this.publishQuote} 
          {...this.state}
        />
      </div>
    );
  }
}

export default App;
