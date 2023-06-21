void hillas()
{
  TString particle_name = "proton";
  TString file_number = "1";
  TFile *file = new TFile("tree_form_out/" + particle_name + "_" + file_number + ".root");
  if (file->IsZombie()) {
    cerr << "Can't read input file!" << endl;
    return;
  }

  TTree *tree = (TTree*)file->Get("tree");
  if (!tree) {
    cerr << "Can't read tree!" << endl;
    return;
  }

  TTree* pixels_tree = (TTree*)file->Get("pixels_tree");
  if (!pixels_tree) {
    cerr << "Can't read input tree!" << endl;
    return;
  }

  int32_t N_pixels;
  int32_t n_buff;
  int32_t amplitude;
  double x_pmt;
  double y_pmt;

  double xpoint[120], ypoint[120];

  tree->SetBranchAddress("N_pixels", &N_pixels);
  tree->SetBranchAddress("N_b_f", &n_buff);
  pixels_tree->SetBranchAddress("amplitude", &amplitude);
  pixels_tree->SetBranchAddress("x_pmt", &x_pmt);
  pixels_tree->SetBranchAddress("y_pmt", &y_pmt);

  TFile* outFile = new TFile("hillas_out_root/hillas_"+ particle_name + "_" + file_number + ".root", "RECREATE");
  TTree* outTree = new TTree("h" + particle_name, "h" + particle_name);
  TTree* outTreeforAlpha = new TTree("size_alpha_nan", "size_alpha_nan");

  Int_t size_alpha_nan;
  Double_t length_alpha_nan = 0.;
  Double_t width_alpha_nan = 0.;
  Double_t dist_alpha_nan = 0.;
  Double_t azwidth_alpha_nan = 0.;
  Double_t miss_alpha_nan = 0.;
  Double_t alpha_alpha_nan = 0.;
  outTreeforAlpha->Branch("size_alpha_nan", &size_alpha_nan, "size_alpha_nan/I");
  outTreeforAlpha->Branch("length_alpha_nan", &length_alpha_nan, "length_alpha_nan/D");
  outTreeforAlpha->Branch("width_alpha_nan", &width_alpha_nan, "width_alpha_nan/D");
  outTreeforAlpha->Branch("dist_alpha_nan", &dist_alpha_nan, "dist_alpha_nan/D");
  outTreeforAlpha->Branch("azwidth_alpha_nan", &azwidth_alpha_nan, "azwidth_alpha_nan/D");
  outTreeforAlpha->Branch("miss_alpha_nan", &miss_alpha_nan, "miss_alpha_nan/D");
  outTreeforAlpha->Branch("alpha_alpha_nan", &alpha_alpha_nan, "alpha_alpha_nan/D");


  Int_t size;
  Double_t length = 0.;
  Double_t width = 0.;
  Double_t dist = 0.;
  Double_t azwidth = 0.;
  Double_t miss = 0.;
  Double_t alpha = 0.;

  outTree->Branch("size", &size, "size/I");
  outTree->Branch("length", &length, "length/D");
  outTree->Branch("width", &width, "width/D");
  outTree->Branch("dist", &dist, "dist/D");
  outTree->Branch("azwidth", &azwidth, "azwidth/D");
  outTree->Branch("miss", &miss, "miss/D");
  outTree->Branch("alpha", &alpha, "alpha/D");

  Int_t start = 0;

  Int_t all_events = tree->GetEntries();
  Int_t normal_dist_events = 0;
  TString filler;
  cout << "start " << endl;

  for (Int_t i=0; i<tree->GetEntries(); i++) {
    tree->GetEntry(i);
    size = n_buff;

    Double_t curXNo = 0.;  
    Double_t curYNo = 0.;  
    Double_t curX2No = 0.;
    Double_t curY2No = 0.;
    Double_t curXYNo = 0.;
    Int_t sum = 0;
    for (Int_t j=start; j<(N_pixels + start); j++) {
      pixels_tree->GetEntry(j);
      sum += amplitude;
      Double_t curWeight = (Double_t)amplitude/n_buff;
      curXNo += curWeight*(Double_t)x_pmt;   // <x>
      curYNo += curWeight*(Double_t)y_pmt;   // <y>
      curX2No += curWeight*(Double_t)x_pmt*x_pmt;   // <x^2>
      curY2No += curWeight*(Double_t)y_pmt*y_pmt;   // <y^2>
      curXYNo += curWeight*x_pmt*y_pmt;             // <xy>
    }

    start += N_pixels;
    if (sum < 10) continue;
    

    /* Calculations */
    Double_t cxx = curX2No - curXNo*curXNo;     // sigma_x^2
    Double_t cyy = curY2No - curYNo*curYNo;     // sigma_y^2
    Double_t cxy = curXYNo - curXNo*curYNo;     // sigma_xy^2
    Double_t d = cyy - cxx;
    Double_t z = TMath::Sqrt(d*d + 4.*cxy*cxy);
    Double_t u = 1. + d/z;
    Double_t v = 2. - u;
    miss = 0.5*(u*curXNo*curXNo + v*curYNo*curYNo) - 2.*cxy*curXNo*curYNo/z;
    



    Double_t checker = curXNo*curXNo + curYNo*curYNo;
    
    

    dist = TMath::Sqrt(checker);
    alpha = asin(miss/dist)*TMath::RadToDeg();
   
   

    //cout << dist << "  ";
    checker = curXNo*curXNo*curY2No - 2.*curXNo*curYNo*curXYNo + curX2No*curYNo*curYNo;
    if (dist != 0. and checker > 0) {
      azwidth = TMath::Sqrt(checker / dist / dist);
    }
    


    length = TMath::Sqrt(0.5*(cxx + cyy + z));
    width = TMath::Sqrt(0.5*(cxx + cyy - z));


    outTree->Fill();

    if (isnan(alpha))
    {
      normal_dist_events++;
      size_alpha_nan = size;
      length_alpha_nan = length;
      width_alpha_nan = width;
      dist_alpha_nan = dist;
      azwidth_alpha_nan = azwidth;
      miss_alpha_nan = miss;
      alpha_alpha_nan = alpha;

      outTreeforAlpha->Fill();
    }

    if (i < 50)
    { 
      cout << "asin(miss/dist) " << miss << " " << dist << " " << asin(miss/dist) << endl;
    }
    if (i < 50)
    {
      //cout << size << " " << length << " " << width << " " << dist << " " << azwidth << " " << miss << " " << alpha << endl;
            
    }
  }


  outTree->Write();
  outTreeforAlpha->Write();
  cout << "nan_alpha_events: " << normal_dist_events << ", all: " << all_events << endl;
}


/*
i: 0
NAN line: 75 12.8038 2.80548 nan 0 0 0
i: 1
NAN line: 42 8.15235 2.00834 nan 0 0 0
i: 3
NAN line: 33 11.6155 2.74281 nan 0 0 0
i: 4
NAN line: 20 11.2131 3.55335 nan 0 0 0
i: 5
NAN line: 38 6.5294 2.21143 nan 0 0 0
i: 6
NAN line: 58 7.69056 2.47105 nan 0 0 0
i: 7
NAN line: 201 17.0399 4.91812 nan 0 0 0
i: 8
NAN line: 61 16.9414 4.41867 nan 0 0 0
i: 9
NAN line: 27 10.7807 4.46315 nan 0 0 0
i: 10
NAN line: 78 16.4932 2.59312 nan 0 0 0
i: 11
NAN line: 87 11.9353 3.56674 nan 0 0 0
i: 12
NAN line: 297 15.1164 4.35572 nan 0 0 0
i: 13
NAN line: 181 15.2071 5.31594 nan 0 0 0
i: 14
NAN line: 446 12.6835 3.49912 nan 0 0 0
i: 15
NAN line: 483 16.4548 4.35131 nan 0 0 0
i: 16
NAN line: 1396 12.4912 4.49629 nan 0 0 0
*/