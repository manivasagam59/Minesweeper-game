#include<iostream>
#include<string.h>
#include<conio.h>
using namespace std;

//Function Declaration
void GameHedder();
void Layout_();
void Layout_line_drawer();
void line_calculator();
void Char_Output_printer();
void Int_Output_printer();
void Character_Array_value_fixer();
int Move_Checker();
void Cursor_Swapper(int RowAdjest,int ColumnAdjest);
void Boom_Hind_Creator();
int EmptySpaceOpener(int I,int J);
void Game_Win();
void Game_Over();
void Game_Over_Generator();

//Global Declaration
int Row=10;
int Column=10;
string Name;
string Line;
bool Game_Status=true;
char Move_Input;

int TotalShell=Row*Column;
int ClosedSpace=TotalShell;
int OpenSpace;
int BoomCount;

//cursor
int CursorRowIndex=0;
int CursorColumnIndex=0;
char TempCursorCharacter;

//global Array declaration
const int ConstRow=10;
const int ConstColumn=10;
char Character_Array[ConstRow][ConstColumn];
//int Integer_Array[ConstRow][ConstColumn];         // -1 - boom , 

int Integer_Array[ConstRow][ConstColumn]={
    {-1,0,0,0,0,0,0,0,-1,0},
    {0,0,0,0,0,0,0,0,0,0},
    {0,0,-1,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,-1,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,-1,0},
    {0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0}
};

//Main
int main(){
    cout<<"Enter Your Name : ";
    cin>>Name;
    line_calculator();
    Character_Array_value_fixer();
    Boom_Hind_Creator();
    //Char_Output_printer();

    getch();
    //Game Run Loop
    while(Game_Status){
        Layout_();
        Move_Input=getch();
        Move_Checker();
        

        //Char_Output_printer();
        //cout<<"\n";
        //Int_Output_printer();
    }

    //for testing pupose
    //getch();
    //system("cls");
    //Char_Output_printer();
    //Int_Output_printer();
    
}

//Functions - Initial value generator --------------------------------------------------------------
void Character_Array_value_fixer(){
    for(int a=0;a<ConstRow;a++){
        for(int b=0;b<ConstColumn;b++){
            Character_Array[a][b]=char(254);
        }
    }
}

void Boom_Hind_Creator(){
    //Track boom
    for(int i=0;i<ConstRow;i++){
        for(int j=0;j<ConstColumn;j++){
            if(Integer_Array[i][j]==-1){
                BoomCount++;
                //Insert a value Arround the Boom
                for(int a=-1;a<2;a++){
                    for(int b=-1;b<2;b++){
                        int TempA=i+a;
                        int TempB=j+b;
                        if(TempA>=0&&TempB>=0&&TempA<ConstRow&&TempB<ConstColumn&&Integer_Array[i+a][j+b]!=-1){
                            Integer_Array[TempA][TempB]=Integer_Array[TempA][TempB]+1;
                        }
                    }
                }
                /*
                Integer_Array[i-1][j-1]=Integer_Array[i-1][j-1]+1;
                Integer_Array[i-1][j]=Integer_Array[i-1][j]+1;
                Integer_Array[i-1][j+1]=Integer_Array[i-1][j+1]+1;
                Integer_Array[i][j+1]=Integer_Array[i][j+1]+1;
                Integer_Array[i+1][j+1]=Integer_Array[i+1][j+1]+1;
                Integer_Array[i+1][j]=Integer_Array[i+1][j]+1;
                Integer_Array[i+1][j-1]=Integer_Array[i+1][j-1]+1;
                Integer_Array[i][j-1]=Integer_Array[i][j-1]+1;
                */
            }
        }
    }
}


// Function - Cursor Moves --------------------------------------------------------------------------
// Move Input Checker
int Move_Checker(){
    switch(Move_Input){
        case 'a':{
            //cout<<"A pressed";
            Cursor_Swapper(0,-1);
            break;
        }
        case 'w':{
            //cout<<"W pressed";
            Cursor_Swapper(-1,0);
            break;
        }
        case 'd':{
            //cout<<"D pressed";
            Cursor_Swapper(0,1);
            break;
        }
        case 's':{
            //cout<<"S pressed";
            Cursor_Swapper(1,0);
            break;
        }
        case 'o':{
            //check Is boom location
            if(Integer_Array[CursorRowIndex][CursorColumnIndex]==-1&&Character_Array[CursorRowIndex][CursorColumnIndex]!='>'){
                Game_Over();
            }else if(Character_Array[CursorRowIndex][CursorColumnIndex]!='>'){
                if(Integer_Array[CursorRowIndex][CursorColumnIndex]==0&&Character_Array[CursorRowIndex][CursorColumnIndex]==char(254)){
                    EmptySpaceOpener(CursorRowIndex,CursorColumnIndex);
                }else{
                    OpenSpace++;
                    ClosedSpace--;
                    Character_Array[CursorRowIndex][CursorColumnIndex]=char(Integer_Array[CursorRowIndex][CursorColumnIndex]+48);
                    if(Character_Array[CursorRowIndex][CursorColumnIndex]=='0'){
                        Character_Array[CursorRowIndex][CursorColumnIndex]=' ';
                    }
                }
            }
            Game_Win();
            break;
        }
        case 'f':{
            if(Character_Array[CursorRowIndex][CursorColumnIndex]==char(254)||Character_Array[CursorRowIndex][CursorColumnIndex]=='>'){
                if(Character_Array[CursorRowIndex][CursorColumnIndex]==char(254)){
                    Character_Array[CursorRowIndex][CursorColumnIndex]='>';
                }else{Character_Array[CursorRowIndex][CursorColumnIndex]=(254);}
            }
            break;
        }
    }
}

void Cursor_Swapper(int RowAdjest,int ColumnAdjest){
    int SwappingRowIndex=CursorRowIndex+RowAdjest;
    int SwappingColumnIndex=CursorColumnIndex+ColumnAdjest;
    if(SwappingRowIndex>=0&&SwappingColumnIndex>=0&&SwappingRowIndex<ConstRow&&SwappingColumnIndex<ConstColumn){
        CursorRowIndex=SwappingRowIndex;
        CursorColumnIndex=SwappingColumnIndex;
    }
}

//Function - - GUI ----------------------------------------------------------------------------------
//calculate line length
void line_calculator(){
    for(int i=0;i<Column;i++){
        Line=Line+"----";
    }
    Line=Line+"-";
}

// draw a horizontal line
void Layout_line_drawer(){
    cout<<Line<<"\n";
}

// Draw the cell
void Layout_(){
    GameHedder();
    for(int i=0;i<ConstRow;i++){
        Layout_line_drawer();
        cout<<"| ";
        for(int j=0;j<ConstColumn;j++){
            if(CursorRowIndex==i&&CursorColumnIndex==j){
                cout<<'X'<<" | ";
            }else{
                cout<<Character_Array[i][j]<<" | ";
            }
        }
        cout<<"\n";
    }
    Layout_line_drawer();
}

//Functions - debuger and tester functions - --------------------------------------------------------------------
// print 2d Character output
void Char_Output_printer(){
    for(int i=0;i<ConstRow;i++){
        for(int j=0;j<ConstColumn;j++){
            cout<<Character_Array[i][j]<<",";
        }cout<<"\n";
    }
}

//print 2d integer output
void Int_Output_printer(){
    for(int i=0;i<ConstRow;i++){
        for(int j=0;j<ConstColumn;j++){
            cout<<Integer_Array[i][j]<<",";
        }cout<<"\n";
    }
}


//Open empty spaces
int EmptySpaceOpener(int I,int J){
   //checkin boundary
   if(I>=0&&I<ConstRow&&J>=0&&J<ConstColumn){
    //checking empty space in Integer Array && char(245) in Character array
       if(Integer_Array[I][J]==0&&Character_Array[I][J]==char(254)){
           //store space in Empty character array  
           Character_Array[I][J]=' ';
           ClosedSpace--;
           OpenSpace++;
           for(int SignI=-1;SignI<2;SignI++){
               for(int SignJ=-1;SignJ<2;SignJ++){
                   EmptySpaceOpener(I+SignI,J+SignJ);
                   //open end next number Array
                   if(Integer_Array[I+SignI][J+SignJ]!=0&&Character_Array[I+SignI][J+SignJ]==char(254)&&I+SignI>=0&&I+SignI<ConstRow&&J+SignJ>=0&&J+SignJ<ConstColumn){
                    Character_Array[I+SignI][J+SignJ]=char(Integer_Array[I+SignI][J+SignJ]+48);
                    ClosedSpace--;
                    OpenSpace++;
                   }
               }
           }
        }
   } 
}


void GameHedder(){
    system("cls");
    cout<<"------------------------------------------------------------------------"<<endl;
    cout<<"                           MINESWEPPER"<<endl;
    cout<<"------------------------------------------------------------------------"<<endl;
    cout<<"Player Name : "<<Name<<endl;
    cout<<"Total Booms : "<<BoomCount<<endl;
    cout<<"Closed Space : "<<ClosedSpace<<"   Open Space : "<<OpenSpace<<endl;
    cout<<"------------------------------------------------------------------------\n"<<endl;

}


void Game_Win(){
    if(ClosedSpace==BoomCount){
        Layout_();
        cout<<"\n               Game Win\n           Congradulation";
        Game_Status=false;
        getch();
    }
}

void Game_Over(){
    Game_Over_Generator();
    Layout_();
    cout<<"\n             Game Over\n           You Can Do it\n              Retry !";
    Game_Status=false;
    getch();
    
}

void Game_Over_Generator(){
    //Track boom
    for(int i=0;i<ConstRow;i++){
        for(int j=0;j<ConstColumn;j++){
            if(Integer_Array[i][j]==-1){
                Character_Array[i][j]=char(162);
            }
        }
    }
}