import { Search } from "../../components/Search";

export const MainPage = ({ mode }) => {
  return (
    <>
      <div className="flex justify-center">
        <Search/>
      </div>
      <div className="mt-12">
        {mode}
        
        {/* popular */}
        <div className="flex-col flex items-center">
          <div className="mt-9 mb-4 text-3xl">POPULAR</div>
          <div className="h-56 bg-main-white opacity-70 rounded-xl shadow-xl w-4/5 ">
            <div className=" h-1/6 flex justify-start p-3">title</div>
            <div className="h-4/6 flex justify-center p-3">
              content contentcontentcontentcontentcontent
            </div>
            <div className="h-1/6 flex justify-end pb-3 pr-3">author</div>
          </div>
        </div>

        {/* new */}
        <div className="flex-col flex items-center">
          <div className="mt-20 mb-4 text-3xl">NEW</div>
          <div className="w-11/12 bg-new-bg h-full pt-5 pb-5 text-center rounded-lg shadow-lg">
            <div>new contentnew contentnew contentnew contentnew content</div>
          </div>
          <div className="w-11/12 bg-new-bg h-full pt-5 pb-5 mt-5 text-center rounded-lg shadow-lg">
            <div>new contentnew contentnew contentnew contentnew content</div>
          </div>
          <div className="w-11/12 bg-new-bg h-full pt-5 pb-5 mt-5 text-center rounded-lg shadow-lg">
            <div>new contentnew contentnew contentnew contentnew content</div>
          </div>
        </div>

        {/* recommend */}
        <div className="flex-col flex items-center mb-16">
          <div className="mt-14 mb-4 text-3xl">RECOMMEND</div>
          <div className="w-11/12 bg-new-bg h-full pt-5 pb-5 text-center rounded-lg shadow-lg">
            <div>new contentnew contentnew contentnew contentnew content</div>
          </div>
          <div className="w-11/12 bg-new-bg h-full pt-5 pb-5 mt-5 text-center rounded-lg shadow-lg">
            <div>new contentnew contentnew contentnew contentnew content</div>
          </div>
          <div className="w-11/12 bg-new-bg h-full pt-5 pb-5 mt-5 text-center rounded-lg shadow-lg">
            <div>new contentnew contentnew contentnew contentnew content</div>
          </div>
        </div>
      </div>
    </>
  );
};
