import { UnknownProjectPage } from './app.po';

describe('unknown-project App', () => {
  let page: UnknownProjectPage;

  beforeEach(() => {
    page = new UnknownProjectPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
