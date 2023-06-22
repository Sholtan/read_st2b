void write_hillas_text() {
   Int_t size;
   Double_t length = 0.;
   Double_t width = 0.;
   Double_t dist = 0.;
   Double_t azwidth = 0.;
   Double_t miss = 0.;
   Double_t alpha = 0.;

   TString particle = "gamma";
   TString file_number = "0";

   TFile *filegamma = new TFile("hillas_out_root/hillas_" + particle + "_" + file_number + ".root", "READ");
   TTree *hgammatree = (TTree*)filegamma->Get("h" + particle);
   if (!hgammatree) {
      cerr << "Can't read tree!" << endl;
      return;
   }




   hgammatree->SetBranchAddress("size", &size);
   hgammatree->SetBranchAddress("length", &length);
   hgammatree->SetBranchAddress("width", &width);
   hgammatree->SetBranchAddress("dist", &dist);
   hgammatree->SetBranchAddress("azwidth", &azwidth);
   hgammatree->SetBranchAddress("miss", &miss);
   hgammatree->SetBranchAddress("alpha", &alpha);



   Int_t size_nans = 0;
   Int_t length_nans = 0;
   Int_t width_nans = 0;
   Int_t dist_nans = 0;
   Int_t azwidth_nans = 0;
   Int_t miss_nans = 0;
   Int_t alpha_nans = 0;



   ofstream outtextfile("hillas_txt/hillas_" + particle + "_" + file_number + ".txt");

   cout << "\n here\n";
   

   Int_t all_entries =  hgammatree->GetEntries();
   Int_t nan_entries = 0;

   for (Int_t i=0; i<(Int_t)(hgammatree->GetEntries()); i++) {
      hgammatree->GetEntry(i);
      if (size >= 20)
      {
         if (!isnan(size) && !isnan(length) && !isnan(width) && !isnan(dist) && !isnan(azwidth)&& !isnan(miss)&& !isnan(alpha)) 
         {
            outtextfile << size << " " << length << " " << width << " " << dist << " " << azwidth << " " << miss << " " << alpha << endl;
         }
         else
         {
            if (i < 50)
            {
               cout << "i: " << i << endl;
               cout << "NAN line: " << size << " " << length << " " << width << " " << dist << " " << azwidth << " " << miss << " " << alpha << endl;
            
            }
            nan_entries++;

            if (isnan(size)) size_nans++;
            if (isnan(length)) length_nans++;
            if (isnan(width)) width_nans++;
            if (isnan(azwidth)) azwidth_nans++;
            if (isnan(miss)) miss_nans++;
            if (isnan(alpha)) alpha_nans++;  
            if (isnan(dist)) dist_nans++;  
         }
      }
   }
   cout << endl << "DONE\n";
   cout << nan_entries << " nans out of " << all_entries << endl;

   cout << "size_nans: " << size_nans << endl;
   cout << "length_nans: " << length_nans << endl;
   cout << "width_nans: " << width_nans << endl;
   cout << "azwidth_nans: " << azwidth_nans << endl;
   cout << "miss_nans: " << miss_nans << endl;
   cout << "alpha_nans: " << alpha_nans << endl;
   cout << "dist_nans: " << dist_nans << endl;
  
}
