import { render, screen } from '@testing-library/react';
import App from './App';

test('renders hyperspace heading', () => {
  render(<App />);
  const headerElement = screen.getByText(/hyperspace/i);
  expect(headerElement).toBeInTheDocument();
});
