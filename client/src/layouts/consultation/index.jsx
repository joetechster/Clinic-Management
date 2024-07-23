// @mui material components
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

// Material Dashboard 2 React example components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";
import DataTable from "examples/Tables/DataTable";

// Data
import courseTableData from "layouts/consultation/data/consultationsTableData";
import { useState } from "react";
import { fetch_authenticated, PrintReport } from "utils/globals";
import { getUser } from "utils/auth";
import { Button, Icon, IconButton } from "@mui/material";
import { useNavigate } from "react-router-dom";

function Tables() {
  const { user } = getUser();
  const navigate = useNavigate();

  const { columns, rows } = courseTableData((setData) => {
    fetch_authenticated(`/consultation`)
      .then((res) => res.json())
      .then((consultations) => {
        setData(consultations);
      });
  });

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <MDBox pt={6} pb={3}>
        <Grid container spacing={6}>
          <Grid item xs={12}>
            <Card>
              <MDBox
                mx={2}
                mt={-3}
                py={3}
                px={2}
                variant="gradient"
                bgColor="info"
                borderRadius="lg"
                coloredShadow="info"
                sx={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}
              >
                <MDTypography variant="h6" color="white">
                  Clinic Visits
                </MDTypography>
                <Button
                  variant="outlined"
                  color="white"
                  onClick={() => navigate("/consultations/create")}
                >
                  Create
                </Button>
              </MDBox>
              <MDBox pt={3}>
                {user.type === "staff" && (
                  <DataTable
                    table={{ columns, rows }}
                    isSorted={false}
                    entriesPerPage={false}
                    showTotalEntries={false}
                    noEndBorder
                  />
                )}
              </MDBox>
            </Card>
          </Grid>
        </Grid>
      </MDBox>
      <PrintReport />
      <Footer />
    </DashboardLayout>
  );
}

export default Tables;
